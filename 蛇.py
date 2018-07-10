import sys
import pycnnum
import builtins

class 蛇:
	def __init__(self):
		self.分 = 分()
		return

	def 関数(self, name, function=False):
		setattr(self, name, function)
		return self.name

	def 見せて(self, data):
		print(data)

class 分:
	def __init__(self, modules=[], names=[]):
		for module, name in zip(modules, names):
			self.輸入(module, name)

	def 輸入して(self, module, name=False):
		if not name:
			name = module
		__builtins__['__import__'](module)
		setattr(self, name, sys.modules[module])

class 数:
	ロマジ = False 
	〇 = False

	def __init__(self, number):
		if isinstance(number, str):
			self.cval = number
			self.ival = False
		elif isinstance(number, int):
			self.ival = number
			self.cval = False
		else:
			raise TypeError("Not a valid number")

	def get_cval(self):
		if self.cval:
			return self.cval
		else:
			self.cval = pycnnum.num2cn(self.ival, numbering_type='mid', big=False, traditional=True, alt_zero=数.〇, alt_two=False, use_zeros=False)
			return self.cval

	def get_ival(self):
		if self.ival:
			return self.ival
		else:
			self.ival = pycnnum.cn2num(self.cval, numbering_type='mid')
			return self.ival
		
	def __str__(self):
		if 数.ロマジ:
			return str(self.ival)
		else:
			return self.get_cval()
	
	def __int__(self):
		return self.get_ival()


蛇 = 蛇()
分 = 分()
整数 = builtins.int
偽 = False
正 = True
