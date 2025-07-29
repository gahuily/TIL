# MovieTheater 클래스는 모든 영화관이 공통으로 가지는 total_movies변수를 가진다.
    # total_movies 변수를 MovieTheater 클래스에 클래스 변수로 추가한다.
# MovieTheater 클래스는 총 영화 수를 증가시키는 add_movie 클래스 메서드를 가진다
    # add_movie 메서드는 total_movies를 1 증가시키고, 영화 추가 성공 메시지를 반환한다.
# MovieTheater 클래스는 영화관의 정보를 출력하는 description 정적 메서드를 가진다.
    # description 메서드는 아래 문장을 출력한다.
    # '"이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다."
    # "영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다."


# 아래에 코드를 작성하시오.

class MovieTheater:
    total_movies = 0

    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0
    
    def reserve_seat(self):
        if self.reserved_seats < self.total_seats:
            self.reserved_seats += 1
            return('좌석 예약이 완료되었습니다.')
        else:
            return('좌석 예약을 실패하였습니다.')
    
    def current_status(self):
        print(f'{self.name} 영화관의 총 좌석 수: {self.total_seats}')
        print(f'{self.name} 영화관의 예약된 좌석 수: {self.reserved_seats}')

    @classmethod
    def add_movie(cls):
        cls.total_movies += 1
        return f'영화가 성공적으로 추가되었습니다.'
    
    @staticmethod
    def description():
        print('이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다.')
        print('영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다.')

m = MovieTheater('메가박스', 100)
c = MovieTheater('CGV', 150)

print(m.reserve_seat())
print(m.reserve_seat())
print(c.reserve_seat())

print(m.add_movie())
print(c.add_movie())

m.current_status()
c.current_status()

print(f'총 영화 수: {c.total_movies}')

MovieTheater.description()