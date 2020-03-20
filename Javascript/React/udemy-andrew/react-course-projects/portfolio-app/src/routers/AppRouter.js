import React from 'react';
import ExpenseDashboardPage from '../Pages/ExpenseDashboardPage';
import AddExpensePage from '../Pages/AddExpensePage';
import HelpPage from '../Pages/HelpPage';
import NotFoundPage from '../Pages/NotFoundPage';
import EditExpensePage from '../Pages/EditExpensePage';
import Header from '../components/Header';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

const AppRouter = () => (
  <BrowserRouter>
    <div>
      <Header />
      <Switch>
        <Route path="/" component={ExpenseDashboardPage} exact={true}></Route>
        <Route path="/create" component={AddExpensePage} ></Route>
        <Route path="/edit/:id" component={EditExpensePage} ></Route>
        <Route path="/help" component={HelpPage} ></Route>
        <Route component={NotFoundPage} ></Route>
      </Switch>
    </div>
  </BrowserRouter>
);

export default AppRouter;