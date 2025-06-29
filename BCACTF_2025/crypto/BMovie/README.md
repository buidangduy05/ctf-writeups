### BMovie
### DESCRIPTION
> I cannot possibly Blieve that you could break into my highly secured, bee-crypted vault
### SOLVED
![image](https://github.com/buidangduy05/ctf-writeups/blob/main/BCACTF_2025/crypto/BMovie/main.png)
> Challenge này yêu cầu chúng ta đăng nhập tài khoản admin để lấy flag
> Nhìn vào đoạn mã trong hình ảnh, thì ta thấy nó sẽ cố gắng chặn chúng ta khi chúng ta đăng nhập đúng username hoặc password của tài khoản admin
> Tuy nhiên khi chúng ta nhìn vào hàm verify ### verify(encoder.encode(user + ";" + password)
