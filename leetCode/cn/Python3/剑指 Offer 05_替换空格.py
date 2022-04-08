# @algorithm @lc id=100280 lang=python3
# @title ti-huan-kong-ge-lcof


from cn.Python3.mod.preImport import *

# @test("We are happy.")="We%20are%20happy." 
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ''
        for i in s:
            if i == ' ':
                res += "%20"
            else:
                res += i
        return res