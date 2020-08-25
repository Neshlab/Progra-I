test_list =['a', 'b','c'] #[1 ,2,3,4,5,6]
remove_list = ['b']#[2,3,4,5]

respond = list(filter(lambda i: i not in remove_list, test_list))
print(respond)



    
