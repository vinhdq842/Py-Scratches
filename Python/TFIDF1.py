import os
import math


class Doc:
    '''
    Lớp mô tả một đối tượng văn bản, lớp này có 1 thuộc tính là wordCount kiểu từ điển

    với key là các từ trong văn bản và value là số lần các từ đó xuất hiện trong văn bản

    CHÚ Ý: Để cho đơn giản, mỗi từ trong văn bản được phân cách bởi dấu cách, các từ phân biệt hoa thường...

    Nói chung 2 từ A và B mà A == B nhận giá trị false là khác nhau.
    Ví dụ từ "anh" và "Anh" là khác nhau
          từ "anh." và "anh" là khác nhau

    '''

    def __init__(self, filename):
        self.wordCount = dict()

        self.loadWordCountFromFile(filename)

    def loadWordCountFromFile(self, filename):
        '''
        Hàm thực hiện đọc vào file filename và đếm tần suất xuất hiện các từ rồi đưa vào wordCount

        Hàm này được gọi đến trong hàm dựng, do vậy bắt buộc phải viết đúng hàm này, nếu không các hàm khác sẽ không được
        chấm điểm

        '''

        f = open(filename, "r")
        s = f.read()
        s = s.split()
        for i in s:
            self.wordCount[i] = self.wordCount[i] + 1 if i in self.wordCount else 1


class TFIDF:
    '''
        Lớp mô tả việc tính chỉ số TFIDF cho các từ trong văn bản dựa trên kho văn bản
        Lớp này có 2 thuộc tính là corpusPath và data, trong đó:
        - corpusPath là đường dẫn tới thư mục chứa các tệp văn bản
        - data là một từ điển với key là tên các file văn bản, và value là các đối tượng Doc tương ứng
        với key

    '''

    def __init__(self, corpusPath):
        self.corpusPath = corpusPath

        self.data = dict()

        self.loadCorpus(corpusPath)

    def loadCorpus(self, corpusPath):
        '''

        Hàm thực hiện đọc các file văn bản trong thư mục corpusPath, và xây dựng các đối tượng

        Doc tương ứng và đưa vào data

         Hàm này được gọi đến trong hàm dựng, do vậy bắt buộc phải viết đúng hàm này, nếu không các hàm khác sẽ không được
        chấm điểm

        '''
        for i in os.listdir(corpusPath):
            self.data[i] = Doc(i)

    def tf(self, w, d):
        '''
        Tính và trả về chỉ số tf của từ w trong Doc d (d là 1 đối tượng Doc)
        Công thức tính tf(w,d) như sau:
        - Gọi tfw là số lần w xuất hiện trong d (ví dụ tfw = 3)
        - Gọi tfm là số lần 1 từ bất kỳ xuất hiện nhiều nhất trong d (ví dụ tfm = 6)
        - khi đó tf(w,d) = tfw/tfm (ví dụ 3/6 = 0.5)
        '''
        tfw = d.wordCount[w] if w in d.wordCount else 0
        tfm = 0
        for i in list(d.wordCount.items()):
            tfm = max(tfm, d.wordCount[i[0]])

        return tfw / tfm

    def idf(self, w):
        '''
        Tính và trả chỉ số idf của từ w trong kho văn bản data
        Chỉ số idf của w là idf(w) được tính như sau:
        - Gọi N là số văn bản có trong kho data (ví dụ N = 10)
        - Gọi m là số văn bản trong kho data có chứa từ w (ví dụ m = 3)
        - khi đó: idf(w) = log(N/(1+m)) (ví dụ idf(w) = log(10/(1+3)) = 0.9162907318741551)

        CHÚ Ý DÙNG math.log để tính log
        '''
        n = len(self.data)
        m = 1
        for i in list(self.data.items()):
            if w in i[1].wordCount:
                m += 1
        return math.log(n / m)

    def tfidf(self, w, d):
        '''
        Hàm tính và trả lại chỉ số tfidf của từ w trong văn bản d (d là một đối tượng Doc) trên kho dữ liệu data
        Chỉ số tfidf(w,d) được tính như sau:
        tfidf(w, d) = tf(w,d) * idf(w)
        '''

        return self.tf(w, d) * self.idf(w)

    def getKTopicWordFromCopus(self, k):
        '''
        Hàm thực hiện tính và trả lại danh sách k từ khác nhau có chỉ số tfidf cao nhất trong kho văn bản data

        Danh sách được sắp xếp tăng dần theo thứ tự từ điển mặc định (không cần sắp xếp theo tiếng Việt)

        CHÚ Ý: 2 từ giống nhau trong 2 văn bản khác nhau có thể cùng có chỉ số tfidf trong top k
        từ có chỉ số tfidf cao nhất, tuy nhiên kết quả chỉ lấy 1 từ
        (có nghĩa là trong danh sách kết quả, k từ đôi một khác nhau)
        '''

        dic = {}

        for i in list(self.data.items()):
            for j in i[1].wordCount:
                dic[j] = max(dic[j], self.tfidf(j, i[1])) if j in dic else self.tfidf(j, i[1])

        tmp = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        rs = [a[0] for a in tmp]
        return sorted(rs[:k])
