import React from 'react'

const LoginPopup = ({ show, message }) => {
    return (
        <div className={`login-popup ${show ? 'show' : ''}`}>
            {message}
        </div>
    )

}

export default LoginPopup
