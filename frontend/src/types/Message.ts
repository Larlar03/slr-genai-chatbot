import { PromptAiResponse } from './PromptAiResponse';

export interface Message {
    content: PromptAiResponse | string;
    isSentByUser: boolean;
}
