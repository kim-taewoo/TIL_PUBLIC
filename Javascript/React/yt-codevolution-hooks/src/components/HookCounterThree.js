import React, { useState } from 'react';

function HookCounterThree() {
  const [name, setName] = useState({ firstName: '', lastName: '' });
  return (
    <form action=''>
      <input
        value={name.firstName}
        onChange={({ target: { value } }) =>
          setName({ ...name, firstName: value })
        }
        type='text'
        name=''
        id=''
      />
      <input
        value={name.lastName}
        onChange={({ target: { value } }) =>
          setName({ ...name, lastName: value })
        }
        type='text'
        name=''
        id=''
      />
      <h2>first name: {name.firstName}</h2>
      <h2>last name: {name.lastName}</h2>
      <h2>{JSON.stringify(name)}</h2>
    </form>
  );
}

export default HookCounterThree;
