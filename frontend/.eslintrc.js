module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true,
  },
  extends: [
    'eslint:recommended',
    'plugin:react/recommended',
    'plugin:react-hooks/recommended',
  ],
  parserOptions: {
    ecmaFeatures: {
      jsx: true,
    },
    ecmaVersion: 'latest',
    sourceType: 'module',
  },
  settings: {
    react: {
      version: 'detect',
    },
  },
  rules: {
    'react/react-in-jsx-scope': 'off',
  },
  overrides: [
    {
      // Radix/shadcn wrappers intentionally forward primitive props via ...props.
      // Keep prop contracts enforced for application components outside this directory.
      files: ['src/components/ui/**/*.{js,jsx,ts,tsx}'],
      rules: {
        'react/prop-types': 'off',
      },
    },
  ],
};
