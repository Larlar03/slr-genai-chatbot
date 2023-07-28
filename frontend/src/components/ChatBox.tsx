import React, { useState } from 'react';
import { PromptAi } from 'src/hooks/PromptAi';
import { Message } from 'src/types/Message';
import MessageBox from './MessageBox';
import LoadingMessage from './LoadingMessage';

const ChatBox = ({ sessionId }: { sessionId: string }) => {
    const [message, setMessage] = useState<string>('');
    const [messages, setMessages] = useState<Message[]>([]);
    const [loading, setLoading] = useState<boolean>(false);

    const sendMessage = async (message: string) => {
        setMessages((messages) => {
            return [
                ...messages,
                {
                    content: message,
                    isSentByUser: true,
                },
            ];
        });

        setLoading(true);

        const response = await PromptAi(message, sessionId, `${import.meta.env.VITE_PROMPT_API}`);

        setMessages((messages) => {
            return [
                ...messages,
                {
                    content: response,
                    isSentByUser: false,
                },
            ];
        });
        setLoading(false);
    };

    return (
        <div
            id='ui-container'
            className='bg-[url("assets/kristina-delp.jpg")] bg-cover w-screen h-screen flex justify-center items-center'
        >
            <div className='p-4 bg-white sm:shadow-none sm:rounded-none lg:shadow-lg lg:rounded-lg sm:h-screen sm:w-screen lg:h-auto lg:w-4/6 xl:w-[682px] flex flex-col'>
                <div className='flex flex-col  space-y-6 sm:h-[93%]'>
                    <div className='flex items-center space-x-4'>
                        <div className='w-10 h-10 bg-gradient-to-r from-[#e0c3fc] to-[#8ec5fc] rounded-full mr-2 ' />
                        <h2 className='text-lg font-semibold'>Single-Lens Reflex Chat</h2>
                    </div>
                    <div className='flex flex-col lg:h-[450px] overflow-y-auto mt-0'>
                        {messages.map((message, index) => {
                            return <MessageBox key={index} message={message} />;
                        })}
                        {loading && <LoadingMessage />}
                    </div>
                </div>
                <div className='flex items-center sm:h-[7%] sm:mt-0 lg:mt-2'>
                    <input
                        className='flex-grow px-2 py-1 border border-gray-300 rounded'
                        type='text'
                        value={message}
                        disabled={loading}
                        placeholder='What shutter speed and aperture should I use for portraits?'
                        onChange={(event) => {
                            setMessage(event.currentTarget.value);
                        }}
                        onKeyDown={async (event) => {
                            if (event.key === 'Enter') {
                                event.preventDefault();
                                const message = event.currentTarget.value;
                                sendMessage(message);
                                setMessage('');
                            }
                        }}
                    />
                    <button
                        className='px-4 py-2 ml-2 text-sm font-semibold text-white bg-[#667eea] hover:bg-[#5C75E6] rounded'
                        disabled={loading}
                        onClick={(event) => {
                            event.preventDefault();
                            sendMessage(message);
                            setMessage('');
                        }}
                    >
                        Send
                    </button>
                </div>
            </div>
        </div>
    );
};

export default ChatBox;
