from ansiblelint.rules import AnsibleLintRule
import re

class UseDictItems(AnsibleLintRule):
    id = 'E207'
    shortdesc = 'use "dict.items" instead of "dict.iteritems"'
    description = ''
    tags = ['formatting']
    compiled = re.compile(r'\:\s(.*\.iteritems.*)$', re.IGNORECASE)

    def match(self, file, text):
        m = self.compiled.search(text)
        if m:
            return True
        return False
