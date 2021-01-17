#正确用户信息
user_corrent={'phone':'18684720553','password':'python'}

#错误用户信息
user_incorrent=[{'phone':'','password':'','expected':'请输入手机号'},
                {'phone':123,'password':'','expected':'请输入正确的手机号'}]
#//div[@class='layui-layer-content']
user_unauthorized=[
    {"phone":13884720553,"password":12,"expected":"此账号没有经过授权，请联系管理员!"}]
