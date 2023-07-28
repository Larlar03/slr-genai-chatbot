import React from 'react';
import { Message } from 'src/types/Message';

const MessageBox = ({ message }: { message: Message }) => {
    const response = !message.isSentByUser ? message.content : null;
    const formattedResponse = response?.split('\n');

    return (
        <>
            {message.isSentByUser && (
                <div className='w-[99%] flex items-end justify-end '>
                    <div className='bg-[#F8F6F8] rounded-lg p-2'>
                        <p className='text-gray-900'>{message.content}</p>
                    </div>
                </div>
            )}
            {!message.isSentByUser && (
                <div className='w-[99%] flex flex-row items-end space-x-3 my-4'>
                    <div>
                        <div className='bg-gradient-to-r from-[#e0c3fc] to-[#8ec5fc] w-10 h-10 rounded-full' />
                    </div>
                    <div className='bg-[#F1F0FF] rounded-lg rounded-bl-none p-2 '>
                        {formattedResponse?.map((line: string, i) => {
                            return line === '' ? (
                                <br />
                            ) : (
                                <p key={i} className='text-[#252136]'>
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
