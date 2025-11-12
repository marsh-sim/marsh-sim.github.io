#!/usr/bin/env python3

"""
Appends or updates generated tables to documentation in mavlink/
Doesn't accept configuration arguments by design.
"""

import argparse
from collections import OrderedDict
from datetime import datetime
from os import path as p
import re
import sys
import subprocess
from typing import Dict, Optional

parser = argparse.ArgumentParser()
parser.add_argument('--ignore-errors', action='store_true',
                    help='exit with 0 exit code even if errors found')
args = parser.parse_args()
ignore_errors: bool = args.ignore_errors

# allow running from anywhere
root_p = p.dirname(__file__)

# clone the mavlink repository
if not p.exists(p.join(root_p, 'mavlink-repo')):
    subprocess.check_call(
        ['git', 'clone', 'https://github.com/marsh-sim/mavlink.git', 'mavlink-repo'],
        cwd=root_p)

# update to latest commit on the dialect branch
subprocess.check_call(['git', 'checkout', 'origin/dialect'],
                      cwd=p.join(root_p, 'mavlink-repo'))

# get commit hash
mavlink_hash = subprocess.check_output(
    ['git', 'rev-parse', 'HEAD'],
    cwd=p.join(root_p, 'mavlink-repo')).decode().strip()

# run upstream generator
subprocess.check_call([sys.executable, 'mavlink_gitbook.py'],
                      cwd=p.join(root_p, 'mavlink-repo', 'doc'))

errors_found = False

# append generated tables to each document
for dialect in ['common', 'marsh', 'minimal']:
    out_p = p.join(root_p, 'docs', 'mavlink', dialect + '.md')
    table_p = p.join(root_p, 'mavlink-repo', 'doc',
                     'messages', '_html', dialect + '.html')

    print('Adding tables to:', dialect)

    # if a file with subset names was provided, only include these identifiers
    subset_p = p.join(p.dirname(out_p), dialect + '_subset.txt')
    # set of identifiers to include, and bool if they were found
    subset_ids: Optional[Dict[str, bool]] = None
    if p.exists(subset_p):
        subset_ids = dict()
        with open(subset_p, 'r') as id_file:
            for line in id_file:
                line = line.strip()
                if len(line) > 0 and line[0] != '#':
                    subset_ids[line] = False
        print('only a subset including:', ', '.join(subset_ids))

    out_lines = []
    with open(out_p, 'r') as content_file:
        found_separator = False
        for line in content_file:
            if 'AUTO-GENERATED PART BELOW' in line:
                found_separator = True
                out_lines.append(line)
                break

            out_lines.append(line)
        if not found_separator:
            raise ValueError(
                'line with comment about auto-generated content required', out_p)

    date = datetime.now().replace(microsecond=0)
    out_lines.append('\n## Definition list\n')
    out_lines.append(
        '\nGenerated on {} from commit [{}](https://github.com/marsh-sim/mavlink/tree/{})\n\n'.format(
            date.isoformat(), mavlink_hash[:7], mavlink_hash
        ))

    # simple processing without full XML parsing

    # extract name of enum, command or message
    id_pattern = re.compile(r'<h3 id="([A-Z\d_]+)')
    # last line of any of items above
    end_string = '</table>'

    # extract section name
    section_pattern = re.compile(r'<h2 id="([a-z_]+)')
    # extract reference to any item
    ref_pattern = re.compile(r'<a href="#([A-Z\d_]+)')

    # links which point to other dialects will be changed to mavlink.io
    dialect_link_pattern = re.compile(r'<a href="([A-Za-z\d_]+).md"')

    # where to insert for table of contents
    toc_line = len(out_lines)

    # data to be written in toc
    contents = OrderedDict()
    contents['enums'] = list()
    contents['mav_commands'] = list()
    contents['messages'] = list()

    with open(table_p, 'r') as in_file:
        include_line = True
        current_section = ''
        current_id = ''
        for line in in_file:
            m = re.search(section_pattern, line)
            if m:
                current_section = m.group(1)

            m = re.search(id_pattern, line)
            if m:
                current_id = m.group(1)
                if subset_ids:
                    if current_id not in subset_ids:
                        include_line = False
                    else:
                        subset_ids[current_id] = True
                if include_line:
                    contents[current_section].append(current_id)

            m = re.search(ref_pattern, line)
            if include_line and current_section != "enums" and m and subset_ids:
                if m.group(1) not in subset_ids:
                    print('ERROR: identifier', m.group(1),
                          'referenced in', current_id, 'but not included', file=sys.stderr)
                    errors_found = True

            if include_line:
                out_lines.append(
                    re.sub(dialect_link_pattern,
                           r'<a href="https://mavlink.io/en/messages/\1.html"', line))
            if subset_ids and end_string in line:
                include_line = True
                current_id = ''

    toc_lines = list()
    toc_lines.append('<ul>\n')
    for section, items in contents.items():
        name = section.replace('_', ' ').title()
        toc_lines.append(f' <li><a href="#{section}">{name}</a><ul>\n')
        for item in items:
            toc_lines.append(f'  <li><a href="#{item}">{item}</a></li>\n')
        toc_lines.append(' </ul></li>\n')
    toc_lines.append('</ul>\n')

    # insert the list starting from this position
    out_lines[toc_line:toc_line] = toc_lines

    with open(out_p, 'w') as out_file:
        out_file.writelines(out_lines)

    if subset_ids:
        for id, found in subset_ids.items():
            if not found:
                print('WARNING: did not find identifier', id, 'in', dialect)

if errors_found:
    print('Some errors found, see output above', file=sys.stderr)
    if not ignore_errors:
        exit(1)
