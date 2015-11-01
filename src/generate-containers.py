# This could be better...
containers = {}
for default, number, dist, lib_dir, pg, pil in [
    ('', '2', 'wily', 'python2.7', '9.4', ''),
    ('3', '3', 'wily', 'python3.4', '9.4', 'python3-pil')]:

    containers['Biopython%s' % number] = (
        ['Biopython-Basic', 'Biopython-Run'],
        {'DIST': dist, 'python': 'python%s' % number, 'pg': pg,
         'pythonp': 'python%s' % default,
         'pil': pil, 'python_dir': lib_dir, 'pip': 'pip%s' % number})
    containers['Biopython%s-Notebook' % number] = (
        ['Biopython-Basic', 'Biopython-Run', 'Biopython-nb'],
        {'DIST': dist, 'python': 'python%s' % number, 'pg': pg,
         'pythonp': 'python%s' % default,
         'pil': pil, 'python_dir': lib_dir, 'pip': 'pip%s' % number,
         'ver': '%s' % number})
    containers['Biopython%s-Tutorial' % number] = (
        ['Biopython-Basic', 'Biopython-Run', 'Biopython-basic-tutorial'],
        {'DIST': dist, 'python': 'python%s' % number, 'pg': pg,
         'pythonp': 'python%s' % default,
         'pil': pil, 'python_dir': lib_dir, 'pip': 'pip%s' % number,
         'ver': '%s' % number})
    containers['Biopython%s-Test' % number] = (
        ['Biopython-Basic', 'Biopython-BuildBot'],
        {'DIST': dist, 'python': 'python%s' % number, 'pg': pg,
         'pythonp': 'python%s' % default,
         'pil': pil, 'python_dir': lib_dir, 'pip': 'pip%s' % number})


def generate_container(container, templates, vars):
    w = open(container, 'w')
    w.write('FROM ubuntu:%s\n' % vars['DIST'])
    w.write('MAINTAINER Tiago Antao <tra@popgen.net>\n\n')
    w.write('ENV DEBIAN_FRONTEND noninteractive\n')
    for fname in templates:
        temp_text = open('templates/' + fname).read()
        for var_name, var_replace in vars.items():
            temp_text = temp_text.replace('<' + var_name + '>', var_replace)
        w.write(temp_text)
        w.write('\n')
    w.close()

for name, content in containers.items():
    templates, vars = content
    generate_container(name, templates, vars)
