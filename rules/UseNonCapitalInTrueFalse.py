from ansiblelint.rules import AnsibleLintRule

import re

class UseNonCapitalInTrueFalse(AnsibleLintRule):
    id = 'E604'
    shortdesc = 'true/false should be started from non-capitalized letter'
    description = ''
    tags = ['formatting']

    compiled = re.compile(r'\:\s(True|False)$')

    def match(self, file, text):
        m = self.compiled.search(text)
        if m:
            return True
        return False
