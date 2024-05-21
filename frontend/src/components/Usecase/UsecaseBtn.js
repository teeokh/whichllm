import React from 'react';
import useUsecases from '../hooks/useUsecases.js';
import './UsecaseBtn.css'

const UsecaseBtn = ({ onSelect }) => {
    const { usecases, error } = useUsecases();

    if (error) {
        return <p>{error}</p>;
    }

    return (
        <div className='grid grid-cols-4 align-items-center'>
            {usecases.map((usecase) => (
                <button className='bg-sky-400 text-white font-small p-4 m-1 rounded hover:bg-sky-500' key={usecase.id} onClick={() => onSelect(usecase.id)}>
                    {usecase.name}
                </button>
            ))}
        </div>
    );
};

export default UsecaseBtn;
