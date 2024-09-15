import React from 'react';

const Layout = ({ children }) => {
  return (
    <div className="layout">
      <header>
        <h1>Sistema de Gestión</h1>
      </header>
      <main>{children}</main>
    </div>
  );
};

export default Layout;
