from mrjob.job import MRJob

class MRWordCount(MRJob):

    def mapper(self, _, line):
        # Đọc từng từ từ mỗi dòng của đầu vào
        for word in line.split():
            # Phát ra cặp khóa-giá trị với khóa là từ và giá trị là 1
            yield (word, 1)

    def reducer(self, key, values):
        # Tổng hợp các giá trị cho mỗi từ
        yield (key, sum(values))

if __name__ == '__main__':
    MRWordCount.run()
