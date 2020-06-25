# Enzyme API

Enzyme 을 사용함으로써 React 컴포넌트 테스팅이 훨씬 편해진다. Enzyme 을 안 쓰면 컴포넌트를 포함한 모든 HTML 요소를 일일이 생성하고 그 내부 내용을 알아내 테스트하는 고난도 삽질이 요구된다.

### Enzyme 을 사용하지 않을 때

ReactDOM 으로 직접 그리고, 테스트 할 때도 유용한 기능이 없어 고생하는 상황 발생.

```javascript
import React from 'react';
import { render, unmountComponentAtNode } from 'react-dom';
import App from '../App';

it('shows a comment box', () => {
  const div = document.createElement('div');
  render(<App />, div);
  // 아래 코드는 자식 컴포넌트의 존재여부를 넘어 그 안의 내용까지 체크하므로
  // 좋지 않다. 오직 자식 컴포넌트의 존재만을 체크하는 게 테스트 파일을 나누고 관리할 목적에 맞다. (Enzyme 에 해당 기능이 구현되어 있다.)
  expect(div.innerHTML).toContain('Box for Comment');

  unmountComponentAtNode(div);
});
```

## Enzyme's Renderers

1. Static
   Render the given component and return plain HTML. Static HTML 이기에 클릭 이벤트와 같은 상호작용 테스트가 불가능하다.

1. Shallow
   Render **just** the given component and none of its children. 대상 컴포넌트 안에 다른 자식 컴포넌트가 있다면 그냥 "있다" 정도만 확인가능하다.

1. Full DOM
   Render the component and all of its children + let us modify it afterwards. 상호작용할 수 있는 Object 를 반환하기 때문에 여러 이벤트 테스트도 가능하다. 즉, 완전한 앱을 렌더링한다. `mount` 같은 메서드를 사용하게 되는데, 주의할 점은 가상돔을 형성해서 쓰기 때문에 다른 테스트에 영향을 끼치지 않으려면 각 테스트가 끝날 때마다 `afterEach` 같은 걸로 현 테스트의 영향을 `unmount` 해줘야 한단 것이다.

## beforeEach(() => {})

Jest 에는 모든 테스트 전에 공통적으로 시행되는 것을 따로 모아놓는 기능이 있다. 즉, 어떤 테스트가 실행되기 전에 공통적으로 정의되거나 실행되어야 하는 코드를 따로 모아두고, 각 테스트가 실행되기 전마다 실행해준다. 그게 `beforeEach` 이다. 주의할 점은, 각 테스트 내에서 접근이 필요한 변수는 전역이어야 하기 때문에, `beforeEach` 에서도 전역에 미리 선언된 변수를 두고, 값을 재할당해서 써줘야 한다.

```javascript
let wrapped;

beforeEach(() => {
  wrapped = shallow(<App />);
});
```

## Providing Fake Event

`simulate` 메서드에 흉내낼 이벤트 이름을 첫번째 인자로, 해당 이벤트의 값으로 넘길 객체를 2번째 인자로 넣어 이벤트를 흉내낸다.

```javascript
it('has a text area that users can type in', () => {
  wrapped.find('textarea').simulate('change', {
    target: { value: 'new comment' },
  });
});
```

## Forcing Update

`setState` 는 기본적으로 rerendering 을 실행시키지만, 그 즉시 효과가 적용되는 게 아닌 async 작업이다. 즉, 테스팅에서 업데이트 이후 상황에 추가적인 진행을 하고 싶다면, `wrapped.update()` 와 같이 `update` 메서드를 사용해야 한다.

## Describe

하나의 테스트 파일 내부에 몇 개의 겹치는 내용을 가지고 있는 테스트들이 있고, 그렇다고 그 파일 내 모든 테스트에 겹치는 내용이 아니라면, 공통된 부분이 있는 그 몇 개의 테스트들만 `describe` 로 묶어서 어떤 공통된 부분이 있는 그룹처럼 짝지을 수 있다. 이렇게 하면 좋은 점이, 그 그룹마다 별개의 `beforeEach`, 와 `afterEach` 를 가진다.

## Moxios

Axios 는 Enzyme 이 사용하는 가상 JSDOM 브라우저 환경에서 제대로 request 요청을 하지 못한다. 그래서 Moxios 라는 애로, 정상적인 Axios 요청을 도중에 가로채서, 마치 제대로 된 response 를 받아온 척 흉내낼 수 있다. 그런데 Async 요청과 마찬가지로 Moxios 요청도 가짜 데이터를 반환하는 데까지 시간이 좀 걸린다. 그렇기 때문에 `moxios.wait` 같은 메서드를 활용해서 가짜 response 를 반환하는 시간을 벌어줘야 한다.

### Moxios 사용시 주의할 점

1. `install` 과 `uninstall` 을 `beforeEach` 와 `afterEach` 에 꼭 해주자.
1. `moxios.wait` 내부에 들어갈 내용은 반드시 정상적인 axios 요청을 포함해선 **안** 되며, moxios 반환 값 관련만 있어야 한다.

예시 코드)

```javascript
it('can fetch a list of comments and display them', (done) => {
  // Attempt to render the *entire* App
  const wrapped = mount(
    <Root>
      <App />
    </Root>
  );
  // find the 'fetchComments' button and click it
  // 이게 정상적인 axios 요청을 호출하는 버튼 클릭이며, 이 정상 요청은 반드시 `moxios.wait` 밖에 있어야 한다.
  wrapped.find('.fetch-comments').simulate('click');
  // Introduce a TINY little pause
  // 짧은 주어진 시간 동안 정상 요청을 가로채서 가짜 response 를 반환한다.
  moxios.wait(() => {
    // Expect to find a list of comments!
    let request = moxios.requests.mostRecent();
    request
      .respondWith({
        status: 200,
        response: [
          {
            name: 'Fetched #1',
          },
          {
            name: 'Fetched #2',
          },
        ],
      })
      .then(() => {
        wrapped.update();
        expect(request.config.url).toEqual(
          'http://jsonplaceholder.typicode.com/comments'
        );
        expect(wrapped.find('li').length).toEqual(2);
        done();
        wrapped.unmount();
      });
  });
});
```

## HOC (Higher Order Component)

`react-redux` 의 `connect` 처럼, 다른 컴포넌트를 감싸서 미리 정의된 다른 속성이나 메서드들을 그 감싼 컴포넌트에 부여할 수 있는 컴포넌트들을 말한다.

주의해야 할 점은, 그 감싼 컴포넌트를 반환할 때, 모든 `props` 를 한꺼번에 spread operator 로 모두 들려 보내야 한다는 것이다. 그래야 정상적으로 본래 그 자식 컴포넌트가 받아야 했을 props 와 HOC 가 부여하는 props 모두 줄 수 있다.

```javascript
render() {
  return <ChildComponent {...this.props} />;
}
```

## Redux Middleware

reducer 로 action 객체가 전달되기 전에 그 action 객체를 수정하거나 멈추거나 할 수 있는 기능.

### Browser Debugger

코드 중간에 `debugger` 라고 작성하고 나서 해당 코드가 관련된 동작을 수행하면, `debugger` 가 적힌 시점에서 실행이 멈춘다. 그러면 그 때 브라우저의 console 탭에 해당 시점에서 동작하고 있는 변수 등을 입력해보며 상태 확인이 가능하다. 

