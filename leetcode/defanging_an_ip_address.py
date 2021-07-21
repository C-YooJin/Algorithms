"""
leetcode 1108. Defanging an IP Address
Apple CODING INTERVIEW
"""

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace('.', '[.]')