import './App.css';
import {LoginPage, LandingPage, ClientChat, TherapistChats,Register,Logo} from "./pages/index";

function App() {
  return (
    <main className='App'>
      <header><Logo></Logo></header>
      <LoginPage />
      {/* <LandingPage />
      <ClientChat />
      <TherapistChats /> */}
      {/* <Register /> */}

    </main>

  );
}

export default App;
