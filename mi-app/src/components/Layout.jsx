import React from 'react';

const Layout = ({ children }) => {
  return (
    <div className="layout">
      <header>

      </header>
      <main>{children}</main>
    </div>
  );
};

export default Layout;
