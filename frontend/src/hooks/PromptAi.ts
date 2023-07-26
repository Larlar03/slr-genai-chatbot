import axios from 'axios';
import { v4 as uuidv4 } from 'uuid';
import { PromptAiQuestion } from 'src/types/PromptAiQuestion';
import { PromptAiResponse } from 'src/types/PromptAiResponse';

export const PromptAi = async (messageString: string, apiUrl: string) => {
    // Fix: keep id for session. May created id on re-render in component?
    const chatId = uuidv4();

    console.log(`Sending message: ${messageString}, chatId: ${chatId}`);

    const requestBody: PromptAiQuestion = {
        chatId: chatId,
        message: messageString,
    };

    const response = await axios.post(apiUrl, requestBody).catch((error) => {
        console.error(error);
    });

    return response?.data.answer;
};
