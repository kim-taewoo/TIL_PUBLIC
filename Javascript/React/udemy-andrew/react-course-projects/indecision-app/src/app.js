console.log('app.js is running');


const user = {
  name: 'Taewoo Kim',
  age: 27,
  location: 'Seoul'
};
function getLocation(location) {
  if (location) {
    return <p>Location: {location}</p>;
  }
}
const template = (
  <div>
    <h1>{user.name ? user.name : "Anonymous"}</h1>
    {(user.age && user.age >= 18) && <p>Age: {user.age}</p>}
    {getLocation(user.location)}
  </div>
);

const appRoot = document.getElementById('app');
ReactDOM.render(template, appRoot);
