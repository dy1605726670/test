def main(arr, num):
	'''二分查找算法 找到元素则返回索引 找不到则返回字符串'''

	i = 0  #列表首索引
	j = len(arr) - 1   #列表尾索引
	mid = (i + j) // 2	#中间值索引

	while i <= j:
		mid = (i + j) // 2
		if num > arr[mid]:	# 如果要查找的元素大于中间值

			i = mid + 1  # 首索引的值为 中间值索引 + 1

		elif num < arr[mid]:  # 如果要查找的元素小于中间值

			j = mid - 1  # 尾索引的值为 中间值索引 - 1

		elif num == arr[mid]:  # 直到找到要查找的值为止
			return mid  #返回查找到的元素索引

	else:  # 如果正常退出 则没有查找到
		return "没有查找到该元素"
	

if __name__ == '__main__':
	for i in range(1,12):
		a = main([1,2,3,4,5,6,7,8,9,10], i)
		print("元素 ", i ," 的索引为：", a)