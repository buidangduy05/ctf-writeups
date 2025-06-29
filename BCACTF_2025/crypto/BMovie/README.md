### BMovie
### DESCRIPTION
> I cannot possibly Blieve that you could break into my highly secured, bee-crypted vault
### SOLVED
![image](https://github.com/buidangduy05/ctf-writeups/blob/main/BCACTF_2025/crypto/BMovie/main.png)
> Challenge này yêu cầu chúng ta đăng nhập tài khoản admin để lấy flag
> Nhìn vào đoạn mã trong hình ảnh, thì ta thấy nó sẽ cố gắng chặn chúng ta khi chúng ta đăng nhập đúng username hoặc password của tài khoản admin
> Tuy nhiên khi chúng ta nhìn vào hàm verify(encoder.encode(user + ";" + password) ta thấy nó còn phải kèm thêm dấu ; ở giữa.
> Vậy nên khi kéo lên hàm signUp() để xem thì ta thấy adminHash = hash(encoder.encode(uname + ";" + pwd));
> Như vậy tạo tài khoàn admin, chúng ta chỉ cần nhớ thêm dấu ; vào cuối username hoặc đầu password và lúc lấy flag, đăng nhập lại chỉ cần nhập dúng tên và password và để dấu ; ngược lại là ra flag vì hash cả 2 đều giống nhau, dấu ; về mặt thực tế vẫn nằm giữa password và username. Sau khi nhập xong thì sẽ ra flag
![image](https://github.com/buidangduy05/ctf-writeups/blob/main/BCACTF_2025/crypto/BMovie/BMovies.png)
### FLAG
> bcactf{!_c@n7_BEE_l1ev3_!t_fwrhiu}
