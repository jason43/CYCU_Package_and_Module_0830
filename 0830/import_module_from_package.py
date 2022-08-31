'''
from package import package_module
package_module.print_a()
package_module.print_b()
'''

'''
from package.package_module import print_a, print_b
print_a()
print_b()
'''

# 需要在__init__.py中先處理過後再使用
from package import print_a, print_b
print_a()
print_b()