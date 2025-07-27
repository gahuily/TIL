# Post 클래스를 정의한다.
# Post의 인스턴스 수를 기록할 수 있는 클래스 변수 post_count를 정의하고, 0을 할당한다.
# 생성자 메서드를 정의한다.
    # 생성자 메서드는 게시물의 제목과 내용을 인자로 받는다.
    # 각 인스턴스는 고유한 제목과 내용을 담을 수 있는 title과 content 변수를 가지고, 
    # 인자로 넘겨받은 값을 할당 받는다.
    # 인스턴스가 생성될 때마다 post_count가 1 증가해야 한다.
# 게시물의 내용을 출력하는 show_content 인스턴스 메서드를 정의한다.
# 게시물의 총 개수를 출력하는 total_posts 클래스 메서드를 정의한다.
# 'SNS 게시물'에 대한 설명을 출력하는 description 정적 메서드를 정의한다.
# 2개 이상의 인스턴스를 생성하고, 각 인스턴스의 title과 content를 출력한다.
# Post 클래스의 total_posts 클래스 메서드를 호출하여 게시물의 총 개수를 출력한다.
# description 정적 메서드를 호출한다.

# 아래에 코드를 작성하시오.

class Post:
    post_count = 0

    def __init__(self, title, content):
        self.title = title
        self.content = content
        Post.post_count += 1

    def show_content(self):
        return f'Content: {self.content}'

    @classmethod
    def total_posts(cls):
        return f'Total posts: {cls.post_count}'

    @staticmethod
    def description():
        return f'SNS 게시물은 소셜 네트워크 서비스에서 사용자가 작성하는 글을 의미합니다.'
    
book1 = Post('Fisrt Post', 'This is the content of the first post.')
book2 = Post('Second Post', 'This is the content of the second post.')

print(f'Title: {book1.title}')
print(book1.show_content())
print(f'Title: {book2.title}')
print(book2.show_content())
print(Post.total_posts())
print(Post.description())