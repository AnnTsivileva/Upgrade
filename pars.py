from pyparsing import Word, alphas, ZeroOrMore, Suppress, Optional, nums, alphanums

words = Word(alphas + "_")
num = Word(nums + '.')
data = Word(nums + '-')
time = Word(nums + ':')
code = Word(alphanums)
user = Word(nums + '.')
category = Word(alphas + '_')
sort = Word(alphas + '_')
pay = Word(alphas + '?')
number = Word(nums)
cart_id = Word(nums)
cart_num = Word(nums)
success_pay = ('success_pay_' + cart_num)# success_pay_9790
parse_module = (Suppress('shop_api      |') + data + time + Suppress('[' + code + '] INFO:') + user + Suppress('https://all_to_the_bottom.com/') + 
		Optional(category + Suppress('/') + sort) + Optional(pay + Suppress('_id=') + number + Suppress('&') + Optional(Suppress('amount=') + number + Suppress('&')) 
		+ Suppress('cart_id=') + cart_id) + Optional(success_pay))

def parsim(line):
	return parse_module.parseString(line)