import React from 'react';

const LoadingMessage = () => {
    return (
        <div className='w-full items-end flex justify-end space-x-3 space-y-3 pl-2 m-2 rounded-lg'>
            <div className='flex flex-row items-center bg-blue-300 h-8 text-base px-4 py-1 rounded-br-none rounded-lg'>
                <div className='animate-bounce w-2 h-2 bg-white rounded-full mr-2' />
                <div className='animate-[bounce_1s_infinite_200ms] w-2 h-2 bg-white rounded-full mr-2' />
                <div className='animate-[bounce_1s_infinite_400ms] w-2 h-2 bg-white rounded-full' />
            </div>
            <img src='https://source.unsplash.com/600x600/?kodak' alt='Bot Avatar' className='w-10 h-10 rounded-full' />
        </div>
    );
};

export default LoadingMessage;
