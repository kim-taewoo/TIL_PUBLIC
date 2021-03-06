대부분의 출처: https://github.com/JaeYeopHan/Interview_Question_for_Beginner/tree/master/OS

## CORS

CORS 는 Cross Origin Resource Sharing 의 줄임말. 도메인 주소가 다른 서버에 http request 를 전송하는 것을 이야기 하는데, 예를 들어 naver.com 에서 api.google.com 으로 http request 를 보내면 CORS 다. top level domain 이 다르면 무조건 CORS 로 간주하기 때문에, naver.com 에서 api.naver.com 으로 보내도 CORS 며, 심지어 PORT 만 달라도 CORS 로 간주된다. 

또한 CORS 외에도 CORB(cross origin read blocking) 현상도 있습니다. CORS를 허용했더라도 POST, PUT, DELETE 요청에서 json을 전송하는 경우 요청이 차단됩니다. 이럴 때는 json 대신 www-form-urlencoded 형식으로 데이터를 보내면 됩니다.

## 동시성(Concurrency) 과 병렬성 (Parallelism)

### 동시성 or 병행성(Concurrency)
동시에 실행되는 것처럼 보이는 것.

1. Logical Level에 속한다.
1. Single Core
    - 물리적으로 병렬이 아닌 순차적으로 동작할 수 있다.
    - 실제로는 Time-sharing으로 CPU를 나눠 사용함으로써 사용자가 Concurrency를 느낄 수 있도록 한다.
1. Multi Core
    - 물리적으로 병렬로 동작할 수 있다.
1. Case
    - Mutex, Deadlock


### 병렬성(Parallelism)
실제로 동시에 작업이 처리가 되는 것.

1. Physical(Machine) Level에 속한다.
1. 오직 Multi Core에서만 가능하다.
1. Case
    - OpenMP, MPI, CUDA
1. 병렬성은 데이터 병렬성과 작업 병렬성으로 구분된다.

#### 데이터 병렬성
1. 같은 작업을 병렬처리
1. 전체 데이터를 나누어 서브 데이터들로 만든 뒤, 서브 데이터들을 병렬 처리해서 속도를 높인다. 보통 서브 데이터들은 멀티 코어의 수만큼 쪼갠다.

### 작업 병렬설
1. 서로 다른 작업을 병렬처리
1. 예시: 웹서버.(각 브라우저 요청 내용을 개별 스레드에서 병렬로 처리)

## 프로세스와 스레드

### 프로세스

프로세스는 실행 중인 프로그램으로 디스크로부터 메모리에 적재되어 CPU 의 할당을 받을 수 있는 것을 말한다. 운영체제로부터 주소 공간, 파일, 메모리 등을 할당받으며 이것들을 총칭하여 프로세스라고 한다. 구체적으로 살펴보면 프로세스는 함수의 매개변수, 복귀 주소와 로컬 변수와 같은 임시 자료를 갖는 **프로세스 스택**과 전역 변수들을 수록하는 **데이터 섹션**을 포함한다. 또한 프로세스는 프로세스 실행 중에 동적으로 할당되는 메모리인 **힙을 포함**한다.

### 스레드(thread)
프로세스 내 실행 단위. 하나일 경우 싱글 스레드(Single thread), N개일 경우 멀티 스레드(Multi thread)라고 함
_출처: https://prohannah.tistory.com/59 [Hello, Hannah!]

스레드는 프로세스의 실행 단위라고 할 수 있다. 한 프로세스 내에서 동작되는 여러 실행 흐름으로 프로세스 내의 주소 공간이나 자원을 공유할 수 있다. 스레드는 스레드 ID, 프로그램 카운터, 레지스터 집합, 그리고 스택으로 구성된다. 같은 프로세스에 속한 다른 스레드와 코드, 데이터 섹션, 그리고 열린 파일이나 신호와 같은 운영체제 자원들을 공유한다. 하나의 프로세스를 다수의 실행 단위로 구분하여 자원을 공유하고 자원의 생성과 관리의 중복성을 최소화하여 수행 능력을 향상시키는 것을 멀티스레딩이라고 한다. 이 경우 각각의 스레드는 독립적인 작업을 수행해야 하기 때문에 각자의 스택과 PC 레지스터 값을 갖고 있다.

#### 스택을 스레드마다 독립적으로 할당하는 이유
스택은 함수 호출 시 전달되는 인자, 되돌아갈 주소값 및 함수 내에서 선언하는 변수 등을 저장하기 위해 사용되는 메모리 공간이므로 스택 메모리 공간이 독립적이라는 것은 독립적인 함수 호출이 가능하다는 것이고 이는 독립적인 실행 흐름이 추가되는 것이다. 따라서 스레드의 정의에 따라 독립적인 실행 흐름을 추가하기 위한 **최소 조건**으로 **독립된 스택**을 할당한다.

#### PC Register 를 스레드마다 독립적으로 할당하는 이유
PC 값은 스레드가 명령어의 어디까지 수행하였는지를 나타나게 된다. 스레드는 CPU 를 할당받았다가 스케줄러에 의해 다시 선점당한다. 그렇기 때문에 명령어가 연속적으로 수행되지 못하고 어느 부분까지 수행했는지 기억할 필요가 있다. 따라서 PC 레지스터를 독립적으로 할당한다.

> 레지스터란? CPU 만이 쓸 수 있는 변수로, 처리 중인 중간 결과를 일시적으로 저장하기 위해 사용하는 고속의 기억회로다.

### 멀티 스레딩의 장점
프로세스를 이용하여 동시에 처리하던 일을 스레드로 구현할 경우 메모리 공간과 시스템 자원 소모가 줄어들게 된다. 스레드 간의 통신이 필요한 경우에도 별도의 자원을 이용하는 것이 아니라 전역 변수의 공간 또는 동적으로 할당된 공간인 Heap 영역을 이용하여 데이터를 주고받을 수 있다. 그렇기 때문에 프로세스 간 통신 방법에 비해 스레드 간의 통신 방법이 훨씬 간단하다. 심지어 스레드의 context switch 는 프로세스 context switch 와는 달리 캐시 메모리를 비울 필요가 없기 때문에 더 빠르다. 따라서 시스템의 throughtput 이 향상되고 자원 소모가 줄어들며 자연스럽게 프로그램의 응답 시간이 단축된다. 이러한 장점 때문에 여러 프로세스로 할 수 있는 작업들을 하나의 프로세스에서 스레드로 나눠 수행하는 것이다.

### 멀티 스레딩의 문제점
멀티 프로세스 기반으로 프로그래밍할 때는 프로세스 간 공유하는 자원이 없기 때문에 동일한 자원에 동시에 접근하는 일이 없었지만 멀티 스레딩을 기반으로 프로그래밍할 때는 이 부분을 신경써줘야 한다. 서로 다른 스레드가 데이터와 힙 영역을 공유하기 때문에 어떤 스레드가 다른 스레드에서 사용중인 변수나 자료구조에 접근하여 엉뚱한 값을 읽어오거나 수정할 수 있다.

그렇기 때문에 멀티스레딩 환경에서는 동기화 작업이 필요하다. 동기화를 통해 작업 처리 순서를 컨트롤 하고 공유 자원에 대한 접근을 컨트롤 하는 것이다. 하지만 이로 인해 병목현상이 발생하여 성능이 저하될 가능성이 높다. 그러므로 과도한 락으로 인한 병목현상을 줄여야 한다.

### 멀티 스레드 vs 멀티 프로세스
멀티 스레드는 멀티 프로세스보다 적은 메모리 공간을 차지하고 문맥 전환이 빠르다는 장점이 있지만, 오류로 인해 하나의 스레드가 종료되면 전체 스레드가 종료될 수 있다는 점과 동기화 문제를 안고 있다. 반면 멀티 프로세스 방식은 하나의 프로세스가 죽더라도 다른 프로세스에는 영향을 끼치지 않고 정상적으로 수행된다는 장점이 있지만, 멀티 스레드보다 많은 메모리 공간과 CPU 시간을 차지한다는 단점이 존재한다. 이 두 가지는 동시에 여러 작업을 수행한다는 점에서 같지만 적용해야 하는 시스템에 따라 적합/부적합이 구분된다. 따라서 대상 시스템의 특징에 따라 적합한 동작 방식을 선택하고 적용해야 한다.

## 스케쥴러

프로세스를 스케줄링하기 위한 Queue 에는 세 가지 종류가 존재한다.

1. Job Queue : 현재 시스템 내에 있는 모든 프로세스의 집합
1. Ready Queue : 현재 메모리 내에 있으면서 CPU 를 잡아서 실행되기를 기다리는 프로세스의 집합
1. Device Queue : Device I/O 작업을 대기하고 있는 프로세스의 집합

## 브라우저 주소창에 url 입력시 어떤 일이 일어나는가
[참고포스팅](https://medium.com/@maneesha.wijesinghe1/what-happens-when-you-type-an-url-in-the-browser-and-press-enter-bb0aa2449c1a)

1. 브라우저의 주소창에 url 입력
1. 브라우저는 총 4가지 캐시를 순서대로 점검하면서 캐시에서 DNS(Domain Name System) 레코드를 확인하여 IP 주소를 찾음. 
    1. 브라우저 캐시, 방문했던 웹사이트를 일정기간 보관하고 있다.
    1. OS 캐시. 브라우저가 사용자 OS 에서 `gethostname` 같은 시스템 콜을 해서 레코드를 찾음
    1. Router 캐시. 
    1. ISP(Internet Service Provider, 한국의 KT,SKB,LG u+ 같은) 캐시. 
    1. (없다면 DNS resolver 를 이용해 IP 주소를 알아냄)
1. 브라우저가 서버와 TCP 연결을 시작함
1. 브라우저가 웹 서버에 HTTP 요청을 보냄
1. 서버가 요청을 처리하고 응답을 되돌려보냄
1. 브라우저는 서버가 보낸 HTML 내용을 표시

### 키워드 설명
- DNS(Domain Name System) is a database that maintains the name of the website (URL) and the particular IP address it links to.