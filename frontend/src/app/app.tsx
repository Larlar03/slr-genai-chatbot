// eslint-disable-next-line @typescript-eslint/no-unused-vars
import styles from './app.module.css';
import ChatBox from 'src/components/ChatBox';
import { v4 as uuidv4 } from 'uuid';

const sessionId = uuidv4();

export function App() {
    return (
        <div>
            <ChatBox sessionId={sessionId} />
        </div>
    );
}

export default App;
