import os # operating system

def read_file(file_name):
	products = []
	with open(file_name, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])

	return products

def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = float(input('請輸入商品價格: '))
		products.append([name, price])

	return products

def print_products(products):
	for p in products:
		print(p[0], '的價格是: ', p[1])

def write_to_csv(file_name, products):
	with open(file_name, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	file_name = 'products.csv' # 可以再改寫 file_name = input('input your file name: ')
	if os.path.isfile(file_name):
		print(file_name,'existed')
		products = read_file(file_name)
	else:
		print(file_name, 'not existed')

	products = user_input(products)
	print_products(products)
	write_to_csv(file_name, products)


if __name__ == '__main__':
	main()
