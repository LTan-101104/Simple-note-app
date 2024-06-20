import './App.css'
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom'
import Login from "./pages/Login"
import Register from "./pages/Register"
import Home from "./pages/Home"
import NotFound from "./pages/NotFound"
import ProtectedRoute from "./components/ProtectedRoute"

function Logout() {
  localStorage.clear()
  return <Navigate to="/login" />

}

// function RegisterAndLogout() {
//   //first clear tokens, no old access tokens
//   localStorage.clear()
//   return <Register />
// }


function App() {

  return (
    <BrowserRouter>
      {/*Include all routes inside <Routes />  */}
      <Routes>
        <Route
          path='/'
          element={
            // so that Home is only rendered when we have the access token
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          }
        />

        <Route
          path='/login'
          element={<Login />}
        />


        <Route
          path='/logout'
          element={<Logout />}

        />

        <Route
          path='/register'
          element={<Register />}
        />

        {/* all other undefined paths will lead to NotFound being rendered */}
        <Route
          path='*'
          element={<NotFound />}
        />
      </Routes>
    </BrowserRouter>

  )
}

export default App
