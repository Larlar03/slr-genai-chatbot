import React from 'react';

const LoadingMessage = () => {
    return (
        <div className='flex justify-start w-full pl-2 m-2 rounded-lg'>
            <div className='flex flex-row items-center bg-blue-300 h-8 text-base px-4 py-1 rounded-bl-none rounded-lg'>
                <div className='animate-bounce w-2 h-2 bg-white rounded-full mr-2' />
                <div className='animate-[bounce_1s_infinite_200ms] w-2 h-2 bg-white rounded-full mr-2' />
                <div className='animate-[bounce_1s_infinite_400ms] w-2 h-2 bg-white rounded-full' />
            </div>
        </div>
    );
};

export default LoadingMessage;
