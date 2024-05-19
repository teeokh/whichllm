import React from 'react';
import useUsecases from '../hooks/useUsecases.js';
import './UsecaseBtn.css'

const UsecaseBtn = ({ onSelect }) => {
    const { usecases, error } = useUsecases();

    if (error) {
        return <p>{error}</p>;
    }

    return (
        <div className="App">
            {usecases.map((usecase) => (
                <button className="usecaseBtn"key={usecase.id} onClick={() => onSelect(usecase.id)}>
                    {usecase.name}
                </button>
            ))}
        </div>
    );
};

export default UsecaseBtn;
