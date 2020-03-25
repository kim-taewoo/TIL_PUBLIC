import React from 'react';
import ExpenseList from '../components/ExpenseList';
import ExpenseListFilters from '../components/ExpenseListFilters';

export default () => (
  <div>
    <ExpenseListFilters />
    <ExpenseList />
  </div>
);