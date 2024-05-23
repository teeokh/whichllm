import React from 'react';

const UsecaseIcon = ({ icon, text, onClick, isActive }) => {
    return (
        <button
            className={`flex flex-col items-center cursor-pointer transition-opacity ${isActive ? 'opacity-100' : 'opacity-50'
                }`}
            onClick={onClick}
        >
            {icon} {/* Render the icon */}
            <span className="mt-2">{text}</span> {/* Render the text */}
        </button>
    );
}

export default UsecaseIcon;