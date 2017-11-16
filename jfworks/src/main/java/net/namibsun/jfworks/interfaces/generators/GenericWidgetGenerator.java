package main.java.net.namibsun.jfworks.interfaces.generators;

import java.util.List;

/**
 * Interface that defines the requirements for a GUI framework to generate widgets.
 */
public interface GenericWidgetGenerator {

    /**
     * Generates a Label Widget that displays a string
     * @param labelText The text to be displayed by the widget
     * @return the label widget
     */
    public Object generateLabel(String labelText);

    /**
     * Generates a Label Widget that displays an image
     * @param imagePath The path to the image file
     * @param maintainAspectRatio Can be set to true to maintain the aspect ratio of the image
     * @param width the width of the image
     * @param height the height of the image
     * @return The Image Label Widget
     */
    public Object generateImageLabel(String imagePath, boolean maintainAspectRatio, int width, int height);

    /**
     * Generates a Button with a String displayed on it. It also calls a Runnable command when pressed
     * @param buttonString The string to be displayed on the button
     * @param command The Runnable command to be executed
     * @return The Button widget
     */
    public Object generateButton(String buttonString, Runnable command);

    /**
     * Generates a Text Entry that can be used to query a string from the user
     * @param defaultText The text displayed in the entry by default
     * @param enterCommand A command Runnable run whenever the enter/return key is pressed when the entry is in focus
     * @param onChangedCommand A command Runnable run whenever the entries' content changes
     * @return the generated Text Entry Widget
     */
    public Object generateTextEntry(String defaultText, Runnable enterCommand, Runnable onChangedCommand);

    /**
     *
     * @param EnterCommand
     * @return
     */
    public Object generatePasswordEntry(Runnable EnterCommand);

    /**
     *
     * @param checkBoxTest
     * @param active
     * @return
     */
    public Object generateCheckBox(String checkBoxTest, boolean active);

    /**
     *
     * @param radioButtonText
     * @return
     */
    public Object generateRadioButton(String radioButtonText);

    /**
     *
     * @param initialPercentage
     * @return
     */
    public Object generatePercentageProgressBar(float initialPercentage);

    /**
     *
     * @param optionsList
     * @return
     */
    public Object generateStringComboBox(List<String> optionsList);

    /**
     *
     * @param options
     * @param multiSelectable
     * @return
     */
    public Object generatePrimitiveMultiColumnListBox(String[] options, boolean multiSelectable);

}
