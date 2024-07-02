class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        answers = []
        for email in emails:
            email = email.split('@')
            email[0] = email[0].replace('.','')
            email[0] = email[0].split('+')[0]
            email = email[0] + '@' + email[1]
            if email not in answers:
                answers.append(email)
        return len(answers)
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
result = Solution().numUniqueEmails(emails)
print(result)