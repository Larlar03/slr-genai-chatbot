import React from 'react';
import { Message } from 'src/types/Message';

const MessageBox = ({ message }: { message: Message }) => {
    const response = !message.isSentByUser ? message.content : null;
    const formattedResponse = response?.split('\n');

    return (
        <>
            {message.isSentByUser && (
                <div className='flex items-end justify-end  space-x-3 space-y-3'>
                    <div className='p-2 bg-[#f2f6f8] rounded-lg'>
                        <p className='text-gray-600'>{message.content}</p>
                    </div>
                </div>
            )}
            {!message.isSentByUser && (
                <div className='w-full flex items-end space-x-3 space-y-3'>
                    <div>
                        <div className='w-10 h-10 bg-gradient-to-r from-[#e0c3fc] to-[#8ec5fc] rounded-full mr-2' />
                    </div>
                    <div className='p-2 bg-[#ebf5fe] rounded-lg rounded-bl-none'>
                        {/* <p className='text-blue-600'>{message.content}</p> */}
                        {formattedResponse?.map((line: string, i) => {
                            return line === '' ? (
                                <br />
                            ) : (
                                <p key={i} className='text-black'>
                                    {line}
                                </p>
                            );
                        })}
                    </div>
                </div>
            )}
        </>
    );
};

export default MessageBox;
