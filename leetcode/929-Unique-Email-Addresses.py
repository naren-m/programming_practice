# https://leetcode.com/problems/unique-email-addresses/
# https://leetcode.com/explore/interview/card/google/67/sql-2/3044/


# Unique Email Addresses

class Solution:
    def numUniqueEmails(self, emails):
        s = set()
        for e in emails:
            s.add(self.cleanEmail2(e))
        
        return len(s)
    
    def cleanEmail2(self, email):
        length = len(email)
        e = [''] * length
        p = 0
        for l in email:
            if l == '+': break
            if l == '.': continue
            
            e[p] = l
            p+=1
        
        lp = p

        #  Find position of @
        for l in email:
            if l == '@': break
            p += 1
        
        # Copy domain name to the email from @
        for i in range(p, length):
            e[lp] = email[i]
            lp += 1
            
        print(e)
        return ''.join(e)

    
    def cleanEmail(self, email):
        localname, domain = email.split('@')[0], email.split('@')[1]
        localname = localname.replace('.', '')
        localname = localname.split('+')[0]
        
        return '{}@{}'.format(localname, domain)
    

        
        
tests = [
    {'input': ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"], 'expected': 2},
    {'input': ["a@leetcode.com","b@leetcode.com","c@leetcode.com"], 'expected': 3},
]


s = Solution()

for test in tests:
    n = s.numUniqueEmails(test['input'])
    print('Input: {}, Expected {}, got {}'.format(
        test['input'], test['expected'], n))
    assert n == test['expected']
