//wrapper for routes
import { Navigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";
import api from '../api'
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants";
import { useEffect, useState } from "react";

// eslint-disable-next-line react/prop-types
export default function ProtectedRoute({ children }) {
    //check if we are authorized
    const [isAuthorized, setIsAuthorized] = useState(null)

    useEffect(() => {
        auth().catch(() => {
            setIsAuthorized(false)
        })
    }, [])

    //refrehs token for us
    const refreshToken = async () => {
        const refreshTok = localStorage.getItem(REFRESH_TOKEN)
        try {
            const res = await api.post("/api/token/refresh/", {
                refresh: refreshTok,
            });
            if (res.status === 200) {
                //refreshtoken return a new access token
                localStorage.setItem(ACCESS_TOKEN, res.data.access)
                setIsAuthorized(true)
            }
            else {
                setIsAuthorized(false)
            }
        }
        catch (error) {
            console.error(error)
            setIsAuthorized(false)
        }

    }

    const auth = async () => {
        //check ACCESS_TOKEN
        const token = localStorage.getItem(ACCESS_TOKEN)
        if (!token) { setIsAuthorized(false) }
        const decoded = jwtDecode(token) //decode token
        const tokenExpiration = decoded.exp
        const now = Date.now() / 1000 //divide 1000 to get date in second
        //! ???
        if (tokenExpiration < now) {
            await refreshToken()
        }
        else {
            setIsAuthorized(true)
        }
    }



    if (isAuthorized === null) {
        return <div>Loading...</div>
    }

    return isAuthorized ? <> {children}  </> : <Navigate to="/login" />

}