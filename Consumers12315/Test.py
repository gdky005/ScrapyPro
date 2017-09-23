import re

from Consumers12315 import Utils

# # text = "1234['了文件']老人家了范德萨老家放"
# text = "['健身服务\n                    \n                ']"
#
# start = "['"
# end = "\n"
#
# print(text.find(start))
# print((end).__len__())
# print(text.find(end))
#
#
# print(Utils.sliptStr(text, start, end))
text = "1.fafsasw1.fksafja;"


print(Utils.matchTitle(text))
