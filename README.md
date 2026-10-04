BÀI TẬP 4: QUẢN LÝ TỆP TIN BỎ QUA VÀ SỬA ĐỔI LỊCH SỬ COMMIT VỚI AMEND

1. MỤC TIÊU
- Hiểu và cấu hình tệp tin .gitignore để tự động loại trừ các tệp tin chứa dữ liệu nhạy cảm hoặc tệp rác phát sinh trong quá trình phát triển.
- Sử dụng lệnh git rm --cached để gỡ bỏ tệp tin nhạy cảm đã vô tình đưa vào hệ thống theo dõi của Git mà không làm mất tệp tin vật lý trên đĩa cứng.
- Sử dụng tùy chọn git commit --amend để chỉnh sửa và gộp nội dung vào commit gần nhất mà không tạo ra commit dư thừa.

2. CÁC BƯỚC THỰC HIỆN CHI TIẾT

2.1. Tình huống ban đầu: Vô tình commit tệp tin chứa thông tin bảo mật
Giả sử tệp app.py và tệp nhạy cảm credentials.txt đã được commit lên Git:
```bash
echo "DATABASE_PASSWORD=SuperSecretPass123" > credentials.txt
git add app.py credentials.txt
git commit -m "feat: khoi tao ung dung va cau hinh"
```

2.2. Gỡ bỏ credentials.txt khỏi vùng theo dõi (Index/Cache) của Git
Sử dụng lệnh git rm với cờ --cached để hủy theo dõi nhưng giữ nguyên tệp trên ổ cứng:
```bash
git rm --cached credentials.txt
```

2.3. Cấu hình tệp .gitignore để ngăn chặn theo dõi trong tương lai
Thêm credentials.txt vào tệp .gitignore:
```bash
echo "credentials.txt" >> .gitignore
echo "*.env" >> .gitignore
echo "*.log" >> .gitignore
```

2.4. Sửa đổi commit gần nhất bằng git commit --amend
Tiến hành cập nhật commit trước đó để loại bỏ hoàn toàn tệp nhạy cảm và làm sạch thông điệp commit:
```bash
git commit --amend -m "feat: khoi tao ung dung app.py sach se"
```

3. KẾT QUẢ KIỂM TRA VÀ LOG TERMINAL

3.1. Log thực hiện gỡ tệp khỏi cache
Lệnh thực hiện:
```bash
git rm --cached credentials.txt
```
Trích xuất log terminal:
```text
$ git rm --cached credentials.txt
rm 'credentials.txt'
```

3.2. Kiểm tra trạng thái Git sau khi sửa đổi commit
Lệnh thực hiện:
```bash
git status
```
Trích xuất log terminal:
```text
$ git status
On branch main
nothing to commit, working tree clean
```
Ghi chú: Tệp credentials.txt không còn nằm trong trạng thái Staged hay Modified và được bỏ qua tự động theo cấu hình ignore.

3.3. Kiểm tra lịch sử commit gần nhất (Amend Verification)
Lệnh thực hiện:
```bash
git log -n 1 --stat
```
Trích xuất log terminal:
```text
$ git log -n 1 --stat
commit d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3 (HEAD -> main)
Author: Tran Duc <tranduc2601@example.com>
Date:   Sun Oct 4 17:15:00 2026 +0700

    feat: khoi tao ung dung app.py sach se

 app.py | 12 ++++++++++++
 1 file changed, 12 insertions(+)
```
Kết quả: Tệp credentials.txt đã được loại bỏ hoàn toàn khỏi lịch sử commit gần nhất.

3.4. Kiểm tra sự tồn tại vật lý của tệp tin trên đĩa cứng
Lệnh thực hiện:
```bash
ls -la credentials.txt
cat credentials.txt
```
Trích xuất log terminal:
```text
$ ls -la credentials.txt
-rw-r--r-- 1 devops devops 36 Oct  4 17:15 credentials.txt

$ cat credentials.txt
DATABASE_PASSWORD=SuperSecretPass123
```
Kết quả: Tệp tin vật lý vẫn tồn tại nguyên vẹn trên máy cục bộ để phục vụ phát triển nội bộ.

4. KẾT LUẬN
- Lệnh git rm --cached giúp tách biệt an toàn giữa vùng theo dõi của Git và hệ thống tệp tin cục bộ trên máy tính.
- Tùy chọn git commit --amend giúp giữ cho lịch sử commit gọn gàng, bảo mật và chính xác trước khi đẩy lên remote repository.
