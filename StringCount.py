#Counts the Number of times a string occurs in another string
def count_occurences(main_string,substring):
    count=0
    start_index=0
    while(start_index<len(main_string)):
        index=main_string.find(substring,start_index)
        if index==-1:
            break
        count+=1
        start_index=index+1
    return count
main_string="ababababab ab ab"
substring="ab"
result=count_occurences(main_string,substring)
print(f"the substring'{substring}'occurs{result} times in the main string")
print(main_string.count(substring))
