Full-Stack Technical Assessment
Duration: 1.5 hours

Focus Areas: API Development, Database Design, Frontend Integration

Overview
Build an "Emoji Story Generator" where users can create, share, and translate stories written entirely in emojis. The system will allow creating emoji stories and provide automatic "translations" into regular text.

Task Description
Create a platform where users can compose stories using only emojis. The system will attempt to generate a humorous narrative translation based on the emoji sequence. Users can save their favorite stories and view popular translations.

Technical Requirements
Backend Architecture


API Design
Endpoints for story creation and retrieval
Translation logic implementation
Basic validation rules
Error handling



Data Model
Story Storage
Translation history
Popularity tracking
Basic validation rules
Frontend Implementation
Story Interface
Emoji picker/composer
Live translation preview
Story display with animations
Responsive design
State Management
Composition state
Translation handling
Loading states
Error handling
Data Structures
interface EmojiStory {
 id: string;
 emojiSequence: string[];
 translation: string;
 authorNickname: string;
 likes: number;
 createdAt: Date;
}

interface Translation {
 storyId: string;
 translation: string;
 votes: number;
}

// Translation rules example
interface TranslationRule {
 pattern: string[];
 templates: string[];
}

Core Features
Story Creation
Emoji sequence composer
Live translation preview
Save and share stories
Basic story validation
Translation System
Pattern-based translation
Template sentence generation
Popular translations display
Translation Logic Examples
// Example patterns
const patterns = [
 {
   pattern: ['🏃', '🌧️'],
   templates: [
     '{person} ran from the rain',
     'Quick dash through the storm'
   ]
 },
 {
   pattern: ['🐱', '🐟'],
   templates: [
     'The cat spotted its favorite meal',
     'Feline fishing adventures'
   ]
 }
]

Evaluation Criteria
Backend Implementation (40%)
API design and implementation
Translation logic
Data modeling
Error handling
Frontend Implementation (40%)
Emoji composition interface
State management
User experience
Animation handling
Code Quality (20%)
Code organization
Error handling
Documentation
Testing approach
Time Management Guide
Setup & planning: 15 minutes
Backend implementation: 35 minutes
Frontend implementation: 30 minutes
Testing & cleanup: 10 minutes
