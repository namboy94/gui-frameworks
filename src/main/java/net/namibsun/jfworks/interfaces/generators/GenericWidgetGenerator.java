package main.java.net.namibsun.jfworks.interfaces.generators;

import java.util.List;
import java.util.Set;

/**
 * Interface that defines the requirements for a GUI framework to generate widgets.
 */
public interface GenericWidgetGenerator {

    /**
     *
     * @param labelText
     * @return
     */
    public Object generateLabel(String labelText);

    /**
     *
     * @param imagePath
     * @param maintainAspectRatio
     * @param width
     * @param height
     * @return
     */
    public Object generateImageLabel(String imagePath, boolean maintainAspectRatio, int width, int height);

    /**
     *
     * @param buttonString
     * @param command
     * @return
     */
    public Object generateButton(String buttonString, Runnable command);

    /**
     *
     * @param defaultText
     * @param enterCommand
     * @param onChangedCommand
     * @return
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
