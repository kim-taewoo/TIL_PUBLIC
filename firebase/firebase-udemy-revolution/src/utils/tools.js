export const firebaseLooper = (snapshot) => {
  // 아래 코드는 파이어베이스가 자체 제공하는 forEach 를 사용해서 할 수도 있다.
  // 즉, snapshot.forEach((doc) => ({id: doc.id, ...doc.data()}))
  // 여기서 forEach 는 자바스크립트에서 제공하는 기본 forEach 가 아님을 알아야 한다!
  const data = snapshot.docs.map((doc)=> ({id: doc.id, ...doc.data()}))
  return data;
};
