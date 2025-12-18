# Lab1AndLab2-230018321. 
Các bước triển khai

B1 Tạo cấu trúc thư mục project/src/... gồm 3 phần:
1. src/core: chứa interfaces.py và dataset_loaders.py.
2. src/preprocessing: chứa simple_tokenizer.py và regex_tokenizer.py.
3. src/representations: chứa count_vectorizer.py.

B2 Viết interface cho Tokenizer và Vectorizer.

B3 Triển khai SimpleTokenizer: chia tách từ cơ bản bằng khoảng trắng, bỏ dấu câu đầu cuối.

B4 Triển khai RegexTokenizer: dùng regex để tách từ, số, contraction (isn't), và dấu câu.

B5 Viết CountVectorizer: xây vocabulary và ma trận đếm từ.

B6 Viết dataset_loaders.py để load dữ liệu UD English EWT (.conllu).

B7 Tạo main.py để test tất cả:

Tokenizers trên ví dụ nhỏ.

Tokenizers trên UD sample.

CountVectorizer trên ví dụ nhỏ.

CountVectorizer trên 200 câu UD English EWT.

2. Cách chạy code và ghi log kết quả

Trong Colab:
%cd /content/drive/MyDrive/ColabProjects/project
python main.py 2>&1 | tee run_log.txt
File run_log.txt sẽ lưu lại toàn bộ kết quả chạy.

3. Giải thích kết quả thu được

SimpleTokenizer: cho kết quả gọn, bỏ dấu câu, ví dụ "Hello, world!" → ['hello', 'world'].

RegexTokenizer: chi tiết hơn, giữ dấu câu và contractions, ví dụ "isn't" → ["isn't"].

CountVectorizer (ví dụ nhỏ): tạo vocabulary đúng theo thứ tự alphabet, sinh ma trận đếm chính xác.

Trên UD English EWT:

Vocabulary có ~1500 token cho 200 câu.

Ma trận doc-term size: 200 x 1498.

Kết quả chứng minh tokenizer và vectorizer hoạt động đúng trên dữ liệu thực.

4. Khó khăn gặp phải và cách giải quyết

Khó khăn 1: Lỗi import module (ModuleNotFoundError).
→ Giải pháp: thêm project root vào sys.path trong main.py.

Khó khăn 2: Dataset ban đầu là file .tar.gz.
→ Giải pháp: giải nén bằng tar -xvzf để lấy file .conllu.

Khó khăn 3: Regex tokenizer trả về ký tự lạ như [ trong UD.
→ Giải pháp: chấp nhận giữ nguyên, hoặc có thể lọc thêm nếu cần.

Khó khăn 4: Quản lý project trên Colab/Drive hơi phức tạp.
→ Giải pháp: tạo đúng thư mục trong Drive, sau đó nén toàn bộ project để nộp.

5. Nguồn tham khảo

Universal Dependencies – UD English EWT dataset:
https://github.com/UniversalDependencies/UD_English-EWT

Tài liệu Python re (regex):
https://docs.python.org/3/library/re.html

Slide/lab hướng dẫn: lab1_tokenization.pdf, lab2_count_vectorization.pdf, criteria.pdf.

6. Ghi chú về model

Bài này không sử dụng model có sẵn nào.

Tất cả các lớp SimpleTokenizer, RegexTokenizer, CountVectorizer đều do em tự code lại theo yêu cầu.
